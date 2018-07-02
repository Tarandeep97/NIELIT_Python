def swap_case(S):
    result = ''
    for l in s:
      if l == l.upper():      #True if l is Capital letter 
        result += l.lower()   #l is converted to lower case and concatenated to result
      else:                   #True if l is in Lowercase 
        result += l.upper()   #l is converted to upper case or Capital letter and concat. to result
        
    return(result)
    
if __name__ == '__main__':
    s = input()               #eg.  s = 'sWap CaSe'
    result = swap_case(s)     
    print(result)             #result = 'SwAP cAsE'
