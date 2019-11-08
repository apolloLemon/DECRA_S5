# mini_mvc2_py.txt


class View():
	def user(self,users):
		print(users.find('two'))
#View

class Control:
	def find(self,user):
		return self._look(user)

	def _look(self,user):
		if user in self.users:
			return self.users[user]
		else:
			return 'The data class ({}) has no {}'.format(self.userName(),user)

	def userName(self):
		return self.__class__.__name__.lower()
#Control

class Model(Control):
	users=dict(one='Bob',two='Michael',three='Dave')
#Model

def main():
	users=Model()
	find=View()
	print('--> The user two\'s "real name" is:\n')
	find.user(users)

if __name__=="__main__":
	main()
