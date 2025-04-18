class Car:
    def move(self):
        print('Moving...')

    def stop(self):
        print('Stop')


my_car = Car()
print(isinstance(my_car, Car))
print(my_car.move())


class Comment:
    def __init__(self, text):
        self.text = text
        self.upvote_quantity = 0

    def upvote(self):
        self.upvote_quantity += 1


comment = Comment("Some text")
print(comment.text)
comment.upvote()
print(comment.upvote_quantity)