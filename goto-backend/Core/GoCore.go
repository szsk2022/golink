package Core

import (
	"GoTo/MysqlUtil"
	"log"
	"math/rand"
)

/*
	@Author Roy<i@rayo.cc>
*/

// SelectGolink 从数据库里挑选链接数据
func SelectGolink() LinkData {
	var GoToLink []GotoStr
	err := MysqlUtil.Db.Select(&GoToLink, "select ID, url, user, status from goto where status=?", 1)
	if err != nil {
		log.Println("[ERROR] Exec Failed,err:", err)
		var CacheData LinkData
		CacheData.ID = -1
		CacheData.Url = "https://www.sunzishaokao.com"
		return CacheData
	}
	if len(GoToLink) == 0 {
		var CacheData LinkData
		CacheData.ID = 0
		CacheData.Url = "https://bsz.limenoon.com"
		return CacheData
	}
	randInt := rand.Intn(len(GoToLink))
	var CacheData LinkData
	CacheData.ID = GoToLink[randInt-1].ID
	CacheData.Url = GoToLink[randInt-1].Url
	return CacheData
}
