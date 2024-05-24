package main

import (
	"math/rand"
	"net/http"
	"strconv"
	"time"

	"github.com/gin-gonic/gin"
	"github.com/prometheus/client_golang/prometheus"
	"github.com/prometheus/client_golang/prometheus/promhttp"
)

// Define metrics
var requestTime = prometheus.NewSummaryVec(
	prometheus.SummaryOpts{
		Name: "request_processing_seconds",
		Help: "Time spent processing request",
	},
	[]string{"endpoint"},
)

func init() {
	// Register the metrics with Prometheus
	prometheus.MustRegister(requestTime)
}

// Middleware to record request duration
func MetricsMiddleware() gin.HandlerFunc {
	return func(c *gin.Context) {
		startTime := time.Now()

		// Process the request
		c.Next()

		endTime := time.Now()
		elapsedTime := endTime.Sub(startTime).Seconds()

		// Record the duration
		path := c.Request.URL.Path
		requestTime.WithLabelValues(path).Observe(elapsedTime)
	}
}

func main() {
	// Create a new Gin router
	router := gin.Default()

	// Use the middleware
	router.Use(MetricsMiddleware())

	// Define routes
	router.GET("/slow_endpoint", slowEndpoint)
	router.GET("/fast_endpoint", fastEndpoint)
	router.GET("/metrics", gin.WrapH(promhttp.Handler()))

	// Intentional crash route for testing
	router.GET("/crash", func(c *gin.Context) {
		// Here, we're deliberately causing a panic to crash the server
		panic("Intentional crash for testing purposes")
	})

	// Start the server
	router.Run("0.0.0.0:8000")
}

// Handlers
func slowEndpoint(c *gin.Context) {
	// Simulate a random delay between 0 and 1 second
	randomDelay := rand.Intn(1000)
	time.Sleep(time.Duration(randomDelay) * time.Millisecond)

	c.JSON(http.StatusOK, gin.H{
		"message": "Slow endpoint processed!",
		"delay":   strconv.Itoa(randomDelay) + " milliseconds",
	})
}

func fastEndpoint(c *gin.Context) {
	c.JSON(http.StatusOK, gin.H{
		"message": "Fast endpoint processed!",
	})
}
