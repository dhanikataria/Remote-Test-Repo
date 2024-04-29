// This file does the database operaitons

package models

import (
	"bookstore_project/package/config"

	"github.com/jinzhu/gorm"
)

var db *gorm.DB //pointer to a database session

type Book struct {
	gorm.Model /* gorm.Model is a struct embedded in "Book" struct. This add common info such as ID, */
	/*CreatedAt, UpdatedAt, and DeletedAt to your construct */
	Name        string `gorm:""json:"name"`
	Author      string `json:"author"`
	Publication string `json:"publication"`
}

func init() { // Whenever you have to communicate with database you will need this init funciton (initialization )
	config.Connect()        //This funciton "Connect()" was created in config > app.go file
	db = config.GetDB()     // This function GetDB() was also created in config > app.go
	db.AutoMigrate(&Book{}) /* The AutoMigrate() function in GORM is used to automatically create or
	update database tables to match the structure of Go structs.*/
}

func (b *Book) CreateBook() *Book {
	db.NewRecord(b)
	db.Create(&b)
	return b

}

func GetAllBooks() []Book {
	var books []Book
	db.Find(&books) /* db.Find() is a function which all the records in the table and populate "books slice with it".
	Find() returns in the Go structs format */
	return books
}

func GetBookById(Id int64) (*Book, *gorm.DB) {
	var getBook Book
	db := db.Where("ID=?", Id).Find(&getBook)
	return &getBook, db
}

func DeleteBook(ID int64) Book {
	var book Book
	db.Where("ID=?", ID).Delete(book)
	return book
}
