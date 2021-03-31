def main():
    in_put = open("temps_input.txt", 'r')
    out_put = open("temps_output.txt", 'w')
    time = 0
    while time <15:
        time = time + 1

        C1 = float(in_put.readline())
        F1 = 9/5 * C1 +32
        print(F1,file=out_put)
    out_put.close()
    in_put.close()



main()


