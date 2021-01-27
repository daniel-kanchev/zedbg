from itemadapter import ItemAdapter
import sqlite3


class DatabasePipeline:
    # Database setup
    conn = sqlite3.connect('zedbg.db')
    c = conn.cursor()

    def open_spider(self, spider):
        self.c.execute(""" CREATE TABLE IF NOT EXISTS articles
        (content text) """)

    def process_item(self, item, spider):
        self.c.execute("""SELECT * FROM articles WHERE content = ?""", (item.get('content'), ))
        duplicate = self.c.fetchall()
        if len(duplicate):
            return item

        print("New entry added")

        # Insert values
        self.c.execute("INSERT INTO articles (content)"
                       " VALUES (?)", (item.get('content'), ))
        self.conn.commit()  # commit after every entry

        return item

    def close_spider(self, spider):
        self.conn.commit()
        self.conn.close()
