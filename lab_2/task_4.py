ticket_input = int(input("Ticket number -> "))
ticket = [int(a) for a in str(ticket_input)]

if ticket[0] + ticket[1] + ticket[2] == ticket[3] + ticket[4] + ticket[5]:
    print("Счастливый")
else:
    print("Обычный")
