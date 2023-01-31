package Core

/*
	@Author Roy<i@rayo.cc>
*/

type GotoStr struct {
	ID     int    `db:"ID"`
	Url    string `db:"url"`
	User   string `db:"user"`
	Status int    `db:"status"`
}

type LinkData struct {
	ID  int
	Url string
}
