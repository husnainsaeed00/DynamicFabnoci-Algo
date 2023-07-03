
if __name__ == '__main__':
    def fab(n):
        results= [1,1]
        for i in range(2,n):
            results.append(results[i-1]+results[i-2])
        print(results)
    fab(10)
