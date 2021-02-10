class Users:

	def __init__(self, email):
		self.email = email
		self.name = email[:email.find('@')].replace('.', ' ')
		self.firstname = email[:email.find('.')]
		self.surename = email[email.find('.')+1:email.find('@')]
		self.domain = email[email.find('@')+1:]

	def __str__(self):
		return "Email: {}\nName: {}\nDomain: {}\n".format(self.email, self.name, self.domain)

with open('emails.txt', 'r') as f:
	emails = f.read().splitlines()

email_list = []
for mail in range(len(emails)):
	email_list.append(Users(emails[mail]))

with open('emails_log.txt', 'w') as f:
	for user in range(len(email_list)):
		f.write(str(email_list[user]) + '\n')

		