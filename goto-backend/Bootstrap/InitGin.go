package Bootstrap

import (
	"GoTo/Bootstrap/static"
	"GoTo/Config"
	"embed"
	"github.com/gin-gonic/gin"
	"html/template"
	"log"
	"net/http"
)

/*
	@Author Roy<i@rayo.cc>
*/

//go:embed dist/*.html
var DistStatic embed.FS

func InitGin() {
	r := gin.Default()
	gin.SetMode(gin.ReleaseMode)
	r.Use(GlobalMiddleWare())
	InitWebRule(r)
	tpl := template.Must(template.New("").ParseFS(DistStatic, "dist/*.html"))
	r.SetHTMLTemplate(tpl)
	r.StaticFS("/static", http.FS(static.FSStatic))
	err := r.Run(Config.Web.Address)
	if err != nil {
		log.Println("启动失败")
	}
}
