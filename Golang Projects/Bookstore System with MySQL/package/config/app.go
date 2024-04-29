// Here we will define a GetDB() which returns a variabe "db". GetDB() will help other files or functions can talk database

package config

import (
	"github.com/jinzhu/gorm"
	_ "github.com/jinzhu/gorm/dialects/mysql"
)

var db *gorm.DB // THis is a global variable accessible to both Connect() and GetDB(). db is a pointer to gorm.DB. gorm.DB allows you to connec to SQL database and perform operation

func Connect() { // we will create a function named "Connect" which will make a connection to the database

	d, err := gorm.Open("mysql", "root:root@tcp(127.0.0.1:3306)/books_database") /* open a connection to the database. "mysel"defines the type of
	database with which you want to connect	then i have username and passowrd
	 and table name (books_database) */

	if err != nil {
		panic(err) /* causing the program to stop immediately and unwind the stack. When a panic is triggered, any functions that were in the middle of execution are terminated,
		and their deferred functions are executed before the program stops. */
	}
	db = d
}

func GetDB() *gorm.DB {
	return db
}
