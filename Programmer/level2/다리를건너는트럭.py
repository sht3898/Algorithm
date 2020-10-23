def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0] * bridge_length
    now_weight = 0
    for idx, truck in enumerate(truck_weights):
        now_weight += truck
        while True:
            answer += 1
            if idx != len(truck_weights)-1:
                if now_weight <= weight:
                    bridge.insert(0, truck)
                else:
                    bridge.insert(0, 0)
                now_weight -= bridge.pop()
                break
            else:
                bridge.insert(0, 0)
                now_weight -= bridge.pop()
                if now_weight == 0:
                    break
    return answer