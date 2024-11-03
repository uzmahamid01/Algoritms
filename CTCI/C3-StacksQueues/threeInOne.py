class ThreeStacks:
    def __init__(self, stack_size):
        self.stack_size = stack_size  # Size of each stack
        self.array = [None] * (stack_size * 3)  # Total array size is 3 * stack_size
        self.tops = [-1, -1, -1]  # Stack pointers for the top of each stack (initialized to -1)

    def push(self, stack_num, value):
        # Check if there's space in the stack
        if self.tops[stack_num] < self.stack_size - 1:
            self.tops[stack_num] += 1
            index = stack_num * self.stack_size + self.tops[stack_num]
            self.array[index] = value
        else:
            print(f"Stack {stack_num} is full!")

    def pop(self, stack_num):
        # Check if the stack is empty
        if self.tops[stack_num] == -1:
            print(f"Stack {stack_num} is empty!")
            return None
        else:
            index = stack_num * self.stack_size + self.tops[stack_num]
            value = self.array[index]
            self.array[index] = None  # Clear the popped value
            self.tops[stack_num] -= 1
            return value

    def peek(self, stack_num):
        # Return the top value without popping
        if self.tops[stack_num] == -1:
            print(f"Stack {stack_num} is empty!")
            return None
        else:
            index = stack_num * self.stack_size + self.tops[stack_num]
            return self.array[index]

    def is_empty(self, stack_num):
        return self.tops[stack_num] == -1


# Example usage
stack_size = 3  # Size of each stack
stacks = ThreeStacks(stack_size)

# Pushing elements into each stack
stacks.push(0, 10)  # Push 10 into stack 0
stacks.push(1, 20)  # Push 20 into stack 1
stacks.push(2, 30)  # Push 30 into stack 2

# Pushing more elements into stack 0
stacks.push(0, 11)
stacks.push(0, 12)

# Trying to push into a full stack
stacks.push(0, 13)  # Stack 0 is full!

# Peeking the top of each stack
print("Top of Stack 0:", stacks.peek(0))  # Should be 12
print("Top of Stack 1:", stacks.peek(1))  # Should be 20
print("Top of Stack 2:", stacks.peek(2))  # Should be 30

# Popping elements
print("Popped from Stack 0:", stacks.pop(0))  # Should pop 12
print("Popped from Stack 1:", stacks.pop(1))  # Should pop 20

# Checking if stacks are empty
print("Is Stack 0 empty?", stacks.is_empty(0))
print("Is Stack 1 empty?", stacks.is_empty(1))
