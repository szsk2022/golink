package Config

import (
	_ "embed"
	"flag"
	"gopkg.in/yaml.v2"
	"io/ioutil"
	"log"
	"os"
)

/*
	@Author Roy<i@rayo.cc>
*/

var (
	C          *Config
	Web        WebConfig
	SqlConf    SqlConfig
	GolinkConf GolinkConfig
)

//go:embed config.yaml
var config_example string

var (
	configPath string
)

func init() {
	flag.StringVar(&configPath, "c", "config.yaml", "config path")
	flag.Parse()
	existsbool, _ := exists(configPath)
	if existsbool == false {
		openFile, err := os.OpenFile(configPath, os.O_RDWR|os.O_CREATE|os.O_TRUNC, 777)
		if err != nil {
			log.Println("[ERROR] OpenFile err:", err)
			os.Exit(210)
			return
		}
		_, err = openFile.WriteString(config_example)
		if err != nil {
			log.Println("[ERROR] WriteFile err:", err)
			os.Exit(211)
			return
		}
		openFile.Close()
		os.Exit(0)
	}
	data, err := ioutil.ReadFile(configPath)
	if err != nil {
		log.Fatal("Error reading config file:\r\n" + err.Error())
	}
	C = &Config{}
	err = yaml.Unmarshal(data, C)
	if err != nil {
		log.Fatal("Eror parsing config file:\r\n" + err.Error())
	}
	SqlConf = C.SQLConfig
	Web = C.Web
	GolinkConf = C.Golink
	log.Println("[INFO] 您现在使用的是自编译版本，无法使用更新功能！")
}

func exists(path string) (bool, error) {
	_, err := os.Stat(path)
	if err == nil {
		return true, nil
	}
	if os.IsNotExist(err) {
		return false, nil
	}
	return true, err
}
