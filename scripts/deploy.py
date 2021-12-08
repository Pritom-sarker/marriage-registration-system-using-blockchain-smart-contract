from brownie import Marriage,config,accounts


def deploy(acc):
    print(acc)
    Marriage.deploy({'from': acc},publish_source=True)
    print('Contract Deployed!!!')



def marriage_reg(add,pswd,acc,amnt):
    Mrg = Marriage[-1]
    reg =Mrg.registration(add,pswd,{'from': acc,'value':amnt})
    reg.wait(1)
    print('Marriage registration completed successfully!!')

def number_of_regs():
    Mrg = Marriage[-1]
    print('Number of Registration {}'.format(Mrg.TotalRegistry()))

def varifyMarriage(add1,add2,acc):
    Mrg = Marriage[-1]

    amnt = Mrg.varifyMarriage(add1,add2)
    if amnt >0:
        print( 'Yes they are Married!!')
        print('Wei: ',amnt)
    else:
        print('This Pair is not Married!!')

def divorce(add,pswd,acc):
    Mrg = Marriage[-1]
    Mrg.Divorce(add,pswd,{'from': acc})
    print('Divorce is successful!!')





def main():
    
    acc = accounts.add(config['wallets']['key']['private_key_2'])
    deploy(acc)
    marriage_reg('0x9BBFBB1e84B2562600a9B212a4c40A9024425d3F',9850,acc,100000000000000000)
    #varifyMarriage('0x9BBFBB1e84B2562600a9B212a4c40A9024425d3F','0x5467a52433638705a0697B6eFF70b98CcBE79FA7',acc)
    divorce('0x9BBFBB1e84B2562600a9B212a4c40A9024425d3F',9850,acc)
