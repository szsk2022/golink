package Core

import (
	"encoding/base64"
	"github.com/gin-gonic/gin"
)

/*
@Author Roy<i@rayo.cc>
*/
func Golink(c *gin.Context) {
	LinkData := SelectGolink()
	encodeString := base64.StdEncoding.EncodeToString([]byte(LinkData.Url))
	c.HTML(200, "index.html", gin.H{"siteurl": encodeString, "siteid": LinkData.ID})
}

func Go_Auth(c *gin.Context) {
	c.JSON(200, gin.H{"code": 200, "msg": "success"})
}
