package Config

/*
	@Author Roy<i@rayo.cc>
*/

type Config struct {
	SQLConfig SqlConfig    `yaml:"SQL"`
	Web       WebConfig    `yaml:"Web"`
	Golink    GolinkConfig `yaml:"Golink"`
}

type SqlConfig struct {
	Address      string `yaml:"Address"`
	Port         int    `yaml:"Port"`
	Username     string `yaml:"Username"`
	Password     string `yaml:"Password"`
	DataBaseName string `yaml:"DataBaseName"`
}

type WebConfig struct {
	Address string `yaml:"Address"`
	Logs    bool   `yaml:"Logs"`
	Debug   bool   `yaml:"Debug"`
}

type GolinkConfig struct {
	Debug bool `yaml:"Debug"`
}
