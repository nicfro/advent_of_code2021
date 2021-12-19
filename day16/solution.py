hexa_dec = {"0" : "0000",
            "1" : "0001",
            "2" : "0010",
            "3" : "0011",
            "4" : "0100",
            "5" : "0101",
            "6" : "0110",
            "7" : "0111",
            "8" : "1000",
            "9" : "1001",
            "A" : "1010",
            "B" : "1011",
            "C" : "1100",
            "D" : "1101",
            "E" : "1110",
            "F" : "1111"}

operators = {"0" : "+",
             "1" : "*",
             "2" : "min",
             "3" : "max",
             "5" : ">",
             "6" : "<",
             "7" : "=="}

def evaluate_expression(evaluator, numbers):
    if evaluator == '+':
        return sum(numbers)

    elif evaluator == '*':
        res = 1
        for i in numbers:
            res *= i
        return res

    elif evaluator == 'min':
        return min(numbers)

    elif evaluator == 'max':
        return max(numbers)

    elif evaluator == ">":
        res = ''
        for i in range(len(numbers)-1):
            res += str(numbers[i])+">"
        res += str(numbers[-1])
        return eval(res)

    elif evaluator == "<":
        res = ''
        for i in range(len(numbers)-1):
            res += str(numbers[i])+"<"
        res += str(numbers[-1])
        return eval(res)

    elif evaluator == "==":
        res = ''
        for i in range(len(numbers)-1):
            res += str(numbers[i])+"=="
        res += str(numbers[-1])
        return eval(res)
    
def get_version_and_id(packet):
    version = int(packet[0:3],2)
    packet_type_id = str(int(packet[3:6],2))
    return packet[6:], version, packet_type_id

def parse_literal(packet):
    parse = 1
    number = ''
    length = 0
    while parse:
        current = packet[:5]
        parse = int(current[0])
        number += current[1:]
        packet = packet[5:]
        length += 5
    return packet, int(number, 2)

hex_input = "620D7800996600E43184312CC01A88913E1E180310FA324649CD5B9DA6BFD107003A4FDE9C718593003A5978C00A7003C400A70025400D60259D400B3002880792201B89400E601694804F1201119400C600C144008100340013440021279A5801AE93CA84C10CF3D100875401374F67F6119CA46769D8664E76FC9E4C01597748704011E4D54D7C0179B0A96431003A48ECC015C0068670FA7EF1BC5166CE440239EFC226F228129E8C1D6633596716E7D4840129C4C8CA8017FCFB943699B794210CAC23A612012EB40151006E2D4678A4200EC548CF12E4FDE9BD4A5227C600F80021D08219C1A00043A27C558AA200F4788C91A1002C893AB24F722C129BDF5121FA8011335868F1802AE82537709999796A7176254A72F8E9B9005BD600A4FD372109FA6E42D1725EDDFB64FFBD5B8D1802323DC7E0D1600B4BCDF6649252B0974AE48D4C0159392DE0034B356D626A130E44015BD80213183A93F609A7628537EB87980292A0D800F94B66546896CCA8D440109F80233ABB3ABF3CB84026B5802C00084C168291080010C87B16227CB6E454401946802735CA144BA74CFF71ADDC080282C00546722A1391549318201233003361006A1E419866200DC758330525A0C86009CC6E7F2BA00A4E7EF7AD6E873F7BD6B741300578021B94309ABE374CF7AE7327220154C3C4BD395C7E3EB756A72AC10665C08C010D0046458E72C9B372EAB280372DFE1BCA3ECC1690046513E5D5E79C235498B9002BD132451A5C78401B99AFDFE7C9A770D8A0094EDAC65031C0178AB3D8EEF8E729F2C200D26579BEDF277400A9C8FE43D3030E010C6C9A078853A431C0C0169A5CB00400010F8C9052098002191022143D30047C011100763DC71824200D4368391CA651CC0219C51974892338D0"
packet = "".join([*map(hexa_dec.get, hex_input)])

def parser(packet, version_count):
    out = 0
    packet, version, packet_type_id = get_version_and_id(packet)
    version_count += version
    if packet_type_id == "4":
        packet, out = parse_literal(packet)
    else:
        length_type_id = packet[0]
        packet = packet[1:]
        if length_type_id == "0":
            numbers = []
            sub_packet_length = int(packet[:15], 2)
            packet = packet[15:]
            sub_packets = packet[:sub_packet_length]
            packet = packet[sub_packet_length:]
            parse = True
            while parse:
                sub_packets, l, version_count = parser(sub_packets, version_count)
                numbers.append(l)
                if len(sub_packets) < 6:
                    parse = False
            evaluator = operators[packet_type_id]
            out = evaluate_expression(evaluator, numbers)
        else:
            numbers = []
            number_of_sub_packets = int(packet[:11], 2)
            sub_pack_count = 0
            packet = packet[11:]
            
            while sub_pack_count < number_of_sub_packets:
                packet, l, version_count = parser(packet, version_count)
                sub_pack_count += 1
                numbers.append(l)
                
            evaluator = operators[packet_type_id]
            out = evaluate_expression(evaluator, numbers) 
    return packet, out, version_count
                
print(parser(packet, 0))