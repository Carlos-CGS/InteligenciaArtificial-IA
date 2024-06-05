n = int(input())
matrices = []

for n in range(0, n):
    matrix = input()
    matrices.append(matrix.split(','))

# TODO: Create a function to calculate accuracy and precision metrics
def verificar_acuracia(VP, FP, FN, VN):
  return (VP + VN) / (VP + FP + FN + VN)

def verificar_precisao(VP, FP):
  return VP / (VP + FP)

# TODO: Create a function to find the matrix index with the best combined accuracy and precision
def best_performance(matrices):
    best_index = 0
    best_accuracy = 0
    best_precision = 0
    # TODO: Define Loop through each matrix to calculate metrics
    for index, matrix in enumerate(matrices):
      VP, FP, FN, VN = map(int, matrix)
      # TODO: Define tp, fp fn and tn
      
      accuracy = verificar_acuracia(VP, FP, FN, VN)
      precision = verificar_precisao(VP, FP)
      # TODO: Calculate accuracy and precision
      
      if (accuracy > best_accuracy) or (accuracy == best_accuracy and precision > best_precision):
        best_index = index
        best_accuracy = accuracy
        best_precision = precision
      
      # TODO: Update best metrics if found
       
    return best_index, best_accuracy, best_precision


index, accuracy, precision = best_performance(matrices)
# Print the results
print(f"Índice: {index + 1}")
print(f"Acurácia: {accuracy:.1f}" if accuracy == round(accuracy, 1) else f"Acurácia: {accuracy:.2f}")
print(f"Precisão: {precision:.1f}" if precision == round(precision, 1) else f"Precisão: {precision:.2f}")