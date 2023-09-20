class Person():
    def __init__(self, age: int, name: str):
        self.age = age
        self.name = name
        self.lan_list = []
        self.__hidden_param = 1

    def eat(self, food: str):
        s = 'eat:{}'.format(food)
        return s

    def speak(self):
        # 构造字符串
        sl = ''
        p = ','
        for i, j in enumerate(self.lan_list):
            if i == (len(self.lan_list) - 1):
                p = ''
            sl += ('%s%s' % (j, p))
        s = 'i am {}, {} years old, i can speak {}.'.format(self.name, self.age, sl)
        print(s)

    # 学习新语言ee
    def learn(self, *language: str):
        for i in language:
            self.lan_list.append(i)


class Student(Person):
    def __init__(self,age ,name, leave):
        print('student self:',self)
        super().__init__(age,name)
        self.leave = leave

    def my_leave(self):
        print('now my leave is:',self.leave)

student = Student(20, '小明', 'primary')
student.learn('chinese','english')
student.speak()
student.my_leave()

