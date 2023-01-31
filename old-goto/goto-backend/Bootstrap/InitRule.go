package Bootstrap

import (
	"GoTo/Core"
	"github.com/gin-gonic/gin"
)

/*
	@Author Roy<i@rayo.cc>
*/

func InitWebRule(r *gin.Engine) {
	r.GET("/", Core.Golink)
	r.POST("/auth", Core.Go_Auth)
}
