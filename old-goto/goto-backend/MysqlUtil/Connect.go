package MysqlUtil

import (
	"GoTo/Config"
	_ "embed"
	"fmt"
	_ "github.com/go-sql-driver/mysql"
	"github.com/jmoiron/sqlx"
	"log"
)

var Db *sqlx.DB

/*
	@Author Roy<i@rayo.cc>
*/

//go:embed sql.sql
var DefultSQLText string

func init() {
	dataSourceName := fmt.Sprintf("%s:%s@tcp(%s:%d)/%s", Config.SqlConf.Username, Config.SqlConf.Password, Config.SqlConf.Address, Config.SqlConf.Port, Config.SqlConf.DataBaseName)
	database, err := sqlx.Open("mysql", dataSourceName)
	if err != nil {
		log.Println("[ERROR] Open mysql Failed,", err)
		return
	}
	Db = database
	err = Db.Ping()
	if err != nil {
		log.Println("[ERROR] Mysql err:", err)
		return
	}
	Db.SetMaxOpenConns(50)
}
