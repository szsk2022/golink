package Bootstrap

import (
	"github.com/gin-gonic/gin"
)

/*
	@Author Roy<i@rayo.cc>
*/

// 全局中间件
func GlobalMiddleWare() gin.HandlerFunc {
	sem := make(chan struct{}, 20)
	acquire := func() { sem <- struct{}{} }
	release := func() { <-sem }
	return func(c *gin.Context) {
		acquire()       // before request
		defer release() // after request
		c.Next()
	}
}
