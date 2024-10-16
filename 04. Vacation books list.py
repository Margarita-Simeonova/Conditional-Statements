def vacation_books_list(pages_in_book, pages_per_hour, days):
    days_needed = int((pages_in_book / pages_per_hour) / days)

    return days_needed


book_pages = int(input())
pages = int(input())
days = int(input())
print(vacation_books_list(book_pages, pages, days))
