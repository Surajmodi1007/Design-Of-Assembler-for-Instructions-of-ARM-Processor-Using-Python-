#code
import re
# Define the instruction set
INSTRUCTIONS = {
 'ADC': '0000100100',
 'ADD': '0001100',
 'ADDS': '0001110',
 'ADR': '1010',
 'ADRL': '11110',
 'AND': '0100000000',
 'ASR': '0000101000',
 'B': '1101',
 'BIC': '0100001110',
 'BL': '11110',
 'BLX': '0001001011',
 'BX': '0001001001',
 'CMN': '0100001011',
 'CMP': '00101',
 'EOR': '0100000000',
 'LDM': '11001',
 'LDR': '01101',
 'LSL': '0001101000',
 'LSR': '0001101001',
 'MOV': '00100',
 'MOVS': '00110',
 'MUL': '0000101100',
 'MVN': '0100001111',
 'ORR': '0100001100',
 'POP': '1011110',
 'PUSH': '1011010',
 'REV': '1011101001',
 'REV16': '1011101011',
 'REVSH': '1011101101',
 'ROR': '0100000111',
 'RSB': '00111',
 'SBC': '0000100110',
 'SETEND': '1110000010010000',
 'STM': '11000',
 'STR': '01100',
 'SUB': '00110',
 'SUBS': '00111',
 'SWI': '11011111',
 'TST': '0100001000',
 'UMLAL': '0000111100',
 'UMULL': '0000111000',
}
# Define the data structures
class Instruction:
 def __init__(self, opcode, operands):
 self.opcode = opcode
 self.operands = operands
class Program:
 def __init__(self):
 self.code = []
 def append(self, instruction):
 self.code.append(instruction)
# Write the parser
def parse_instruction(line):
 parts = re.split('[ ,]+', line.strip())
 opcode = INSTRUCTIONS[parts[0]]
 operands = parts[1:]
 return Instruction(opcode, operands)
# Write the assembler
def assemble_instruction(instruction):
 opcode = instruction.opcode
 operands = instruction.operands
 if opcode == INSTRUCTIONS['ADR']:
 # ADR instruction requires special handling
 rd = format(int(operands[0][1:]), '03b')
 immediate = format(int(operands[1]), '08b') 
 machine_code = opcode + rd + immediate
 else:
 # All other instructions have the same format
 rd = format(int(operands[0][1:]), '03b')
 rn = format(int(operands[1][1:]), '03b')
 rm = format(int(operands[2][1:]), '03b') if 
len(operands) > 2 else '000'
 machine_code = opcode + rn + rd + rm
 return machine_code
# Sample usage
program = Program()
program.append(parse_instruction('ADD R1, R2, 
R3'))
program.append(parse_instruction('ADD R1, R2, 
#3'))
program.append(parse_instruction('SUB R4, R5, 
#10'))
program.append(parse_instruction('MOV R0, 
#255'))
program.append(parse_instruction('AND R3, R1, 
R2'))
program.append(parse_instruction('ORR R0, R2, 
R4'))
program.append(parse_instruction('EOR R1, R1, 
R4'))
program.append(parse_instruction('LSL R2, R1, 
#2'))
program.append(parse_instruction('LSR R5, R2, 
#3'))
program.append(parse_instruction('ASR R6, R3, 
#1'))
for instruction in program.code:
 print(‘\n’)
 print(assemble_instruction(instruction))
