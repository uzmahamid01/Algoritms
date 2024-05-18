from pythonds.basic import Queue

def hot_potato(name_list, num):
    sim_queue = Queue()

    for name in name_list:
        sim_queue.enqueue(name)
    
    print(sim_queue)
    while sim_queue.size() > 1:
        for i in range(num):
            sim_queue.enqueue(sim_queue.dequeue())
        sim_queue.dequeue()

    return sim_queue.dequeue()

def main():
    players = ["Bill", "David", "Susan", "Jane", "Kent", "Brad"]
    winner = hot_potato(players, 7)
    print("The winner is:", winner)

if __name__ == "__main__":
    main()
