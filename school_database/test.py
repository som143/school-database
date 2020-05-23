
original_str= 's'
prev_chr = ''
result_str = ''
count = 1
result_str1 = ''
for i in range(len(original_str)):
   if prev_chr == original_str[i]:
       count += 1
       result_str1 = original_str[i] + str(count)
   else:
       if count >  1:
           result_str += result_str1
           count = 1
           
       if count == 1:    
           result_str1 = original_str[i] + str(count)

   prev_chr = original_str[i]
else:
   result_str += result_str1