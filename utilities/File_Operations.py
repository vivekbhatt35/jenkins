class FileOperation:

    def write_to_file(self, content):
        with open(r"C:\Users\rsi\PycharmProjects\LondonWeather\Test_data\Newfile.txt",'w') as file:
            for item in content:
                file.write("%s\n" % item)
                # file.write(content)

    def read_from_file(self):
        with open(r"C:\Users\rsi\PycharmProjects\LondonWeather\Test_data\Newfile.txt", 'r') as file:
            for i in file:
                x= file.read().split('\n')
                x.pop()
                return x

