def twoSensorAvg(input_data, duration=1):
    times = {}
    for i in input_data:
        data = i.split(',')
        time = int(int(data[1]) / (duration * 1000))
        if time not in times:
            times[time] = [0, 0]
        times[time][0] += int(data[2])
        times[time][1] += 1
    ans = []
    for i, v in times.items():
        i = int(i)
        a = str(i * duration * 1000) + '-' + str(i * duration * 1000 + 1000 * (duration - 1) + 999) + ': ' + str(
            round(float(v[0] / v[1]), 2))
        ans.append(a)
    return ans


def test(input, output, duration):
    results = twoSensorAvg(input, duration)
    print(results)
    if len(results) != len(output):
        return False
    for i in range(len(output)):
        if results[i] != output[i]:
            return False
    return True


if __name__ == '__main__':
    input_data = ['1,10000,40', '1,10002,45', '1,11015,50', '2,10005,42', '2,11051,45', '2,12064,42', '2,13161,42']
    ans = ['10000-10999: 42.33', '11000-11999: 47.5', '12000-12999: 42.0', '13000-13999: 42.0']
    print(test(input_data, ans, 1))

