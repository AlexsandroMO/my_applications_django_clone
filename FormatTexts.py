

def format_cpf_cnpj(var, a):
  
  num_str = var.replace('.','')

  print('>>>', num_str)

  #print(len(num_str)-1)

  if (len(num_str)-2) == 2:
    result = '{},{}'.format(num_str[:len(num_str)-2][:3], num_str[len(num_str)-2:])
  elif len(num_str) == 3:
    result = '{},{}'.format(num_str[:len(num_str)-2][:1], num_str[len(num_str)-2:])
  elif (len(num_str)-2) == 3:
    #print('{},{}'.format(num_str[:len(num_str)-2][:3], num_str[len(num_str)-2:]))
    result = '{},{}'.format(num_str[:len(num_str)-2][:3], num_str[len(num_str)-2:])
  elif (len(num_str)-2) == 4:
    #print('aqui = 4')
    #print('{}.{},{}'.format(num_str[:len(num_str)-2][:1], num_str[:len(num_str)-2][1:4], num_str[len(num_str)-2:]))
    result = '{}.{},{}'.format(num_str[:len(num_str)-2][:1], num_str[:len(num_str)-2][1:4], num_str[len(num_str)-2:])
  elif (len(num_str)-2) == 5:
    #print('aqui = 5')
    #print('{}.{},{}'.format(num_str[:len(num_str)-2][:2], num_str[:len(num_str)-2][2:5], num_str[len(num_str)-2:]))
    result = '{}.{},{}'.format(num_str[:len(num_str)-2][:2], num_str[:len(num_str)-2][2:5], num_str[len(num_str)-2:])
  elif (len(num_str)-2) == 6:
    #print('aqui = 6')
    #print('{}.{},{}'.format(num_str[:len(num_str)-2][:3], num_str[:len(num_str)-2][3:6], num_str[len(num_str)-2:]))
    result = '{}.{},{}'.format(num_str[:len(num_str)-2][:3], num_str[:len(num_str)-2][3:6], num_str[len(num_str)-2:])
  elif (len(num_str)-2) == 7: 
    #print('aqui = 7') 
    #print('{}.{}.{},{}'.format(num_str[:len(num_str)-2][:1], num_str[:len(num_str)-2][1:4], num_str[:len(num_str)-2][4:7], num_str[len(num_str)-2:]))
    result = '{}.{}.{},{}'.format(num_str[:len(num_str)-2][:1], num_str[:len(num_str)-2][1:4], num_str[:len(num_str)-2][4:7], num_str[len(num_str)-2:])

  elif (len(num_str)-2) == 8: 
    #print('aqui = 8') 
    #print('{}.{}.{},{}'.format(num_str[:len(num_str)-2][:2], num_str[:len(num_str)-2][1:4], num_str[:len(num_str)-2][4:7], num_str[len(num_str)-2:]))
    result = '{}.{}.{},{}'.format(num_str[:len(num_str)-2][:2], num_str[:len(num_str)-2][1:4], num_str[:len(num_str)-2][4:7], num_str[len(num_str)-2:])

  elif (len(num_str)-2) == 9: 
    #print('aqui = 9') 
    #print('{}.{}.{},{}'.format(num_str[:len(num_str)-2][:3], num_str[:len(num_str)-2][1:4], num_str[:len(num_str)-2][4:7], num_str[len(num_str)-2:]))
    result = '{}.{}.{},{}'.format(num_str[:len(num_str)-2][:3], num_str[:len(num_str)-2][1:4], num_str[:len(num_str)-2][4:7], num_str[len(num_str)-2:])

  print('>>>>>>>>>>>',result, a)
  return result


def cel_tel(var):
  result = ''
  if len(var) == 10:
    result = '({}) {}-{}'.format(var[:2], var[2:6], var[6:])
  elif len(var) == 11:
    result = '({}) {}-{}'.format(var[:2], var[2:7], var[7:])
  
  return result