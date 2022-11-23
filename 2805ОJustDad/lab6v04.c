// 4 - bubble, insert, quick, merge, gnome

#include <stdio.h>
#include <stdlib.h>
#define RFACTOR (1.24733)

int bubbleSort(int n, int *a);
int insertionSort(int n, int *mass);
int mergeSort(int *a, int l, int r);
int gnomeSort(int n, int *a);
int quickSort(int *numbers, int left, int right);

void read_numbers(FILE* input, int size, int* numbers);
int numberCount(FILE* input);
void print_array(int* numbers, int size);

/**
 * Reads a file containing a list of integers and stores them in an array.
 *
 * @param input The file to read.
 * @param size The number of integers in the file.
 * @param numbers The array to store the integers in.
 *
 * @returns None
 */
int main() {
  FILE* input = fopen("l6v04.txt", "r");
  if (input == 0) {
    printf("cant open file\n");
    return 1;
  }
  int size = numberCount(input);
  int numbers[size];
  read_numbers(input, size, numbers);
  int *bubble = numbers;
  int bubbleCount = bubbleSort(size, bubble);
  int *insert = numbers;
  int insertCount = insertionSort(size, insert);
  int *gnome = numbers;
  int gnomeCount =   gnomeSort(size, gnome);
  int *quick = numbers;
  int quickCount = quickSort(quick, 0, size);
  int *merge = numbers;
  int mergeCount = mergeSort(merge, 0, size);
  print_array(insert, size);
  printf("-------------------------------------------------------\n");
  print_array(bubble, size);
  printf("-------------------------------------------------------\n");
  print_array(gnome, size);
  printf("-------------------------------------------------------\n");
  print_array(merge, size);
  printf("-------------------------------------------------------\n");
  print_array(quick, size);
  printf("-------------------------------------------------------\n");
  printf("bubbleCount : %d,\n", bubbleCount);
  printf("insertCount : %d,\n", insertCount);
  printf("gnomeCount : %d,\n", gnomeCount);
  printf("quickCount : %d,\n", quickCount);
  printf("mergeCount : %d,\n", mergeCount);
}

void read_numbers(FILE* input, int size, int* numbers) {
  fseek(input, 0, SEEK_SET);
  for (int i = 0; i < size; ++i) {
    fscanf(input, "%d", &numbers[i]);
  }
}

int numberCount(FILE* input) {
  fseek(input, 0, SEEK_SET);
  int counter = 0;
  while (1) {
    int value;
    if (fscanf(input, "%d", &value) == 1)
      counter++;
    if (feof(input))
      break;
  }
  return counter;
}

void print_array(int* numbers, int size) {
  for (int i = 0; i < size; ++i) {
    printf("%d ; ", numbers[i]);
  }
  printf("\n");
}

int bubbleSort(int n, int *a){
    int i, j;
    int count = 0;
    for(i = 0 ; i < n - 1; i++) {
       for(j = 0 ; j < n - i - 1 ; j++) {
           if(a[j] > a[j+1]) {
              int tmp = a[j];
              a[j] = a[j+1] ;
              a[j+1] = tmp;
              count++;
           }
        }
    }
    return count;
}

int insertionSort(int n, int *mass){
    int newElement, location;
    int count = 0;

    for (int i = 1; i < n; i++)
    {
        newElement = mass[i];
        location = i - 1;
        while(location >= 0 && mass[location] > newElement)
        {
            mass[location+1] = mass[location];
            location = location - 1;
            count++;
        }
        mass[location+1] = newElement;
        count++;
    }
    return count;
}

int mergeSort(int *a, int l, int r)
{
    int count = 0;
    if (l == r) return count; // границы сомкнулись
    int mid = (l + r) / 2; // определяем середину последовательности
    // и рекурсивно вызываем функцию сортировки для каждой половины
    count += mergeSort(a, l, mid);
    count += mergeSort(a, mid + 1, r);
    int i = l;  // начало первого пути
    int j = mid + 1; // начало второго пути
    int *tmp = (int*)malloc(r * sizeof(int)); // дополнительный массив
    for (int step = 0; step < r - l + 1; step++){ // для всех элементов дополнительного массива
        // записываем в формируемую последовательность меньший из элементов двух путей
        // или остаток первого пути если j > r
        if ((j > r) || ((i <= mid) && (a[i] < a[j]))) {
            tmp[step] = a[i];
            count++;
            i++;
        }else {
            tmp[step] = a[j];
            count++;
            j++;
        }
    }
    // переписываем сформированную последовательность в исходный массив
    for (int step = 0; step < r - l + 1; step++){
      a[l + step] = tmp[step];
      count++;
    }
    return count;
}

int gnomeSort(int n, int *a){
	// сортировка
	int i = 1; // счётчик
  int count = 0;
	while (i < n/*если мы не в конце*/) {
		if (i == 0) {
			i = 1;
		}
		if (a[i-1] <= a[i]) {
			++i; // идём вперед
      count++;
		} else {
			// меняем местами
			long tmp = a[i];
			a[i] = a[i-1];
			a[i-1] = tmp;
      count++;
			// идём назад
			--i;
		}
	}
  return count;
}

int quickSort(int *numbers, int left, int right)
{
  int count = 0;
  int pivot; // разрешающий элемент
  int l_hold = left; //левая граница
  int r_hold = right; // правая граница
  pivot = numbers[left];
  while (left < right) // пока границы не сомкнутся
  {
    while ((numbers[right] >= pivot) && (left < right))
      right--; // сдвигаем правую границу пока элемент [right] больше [pivot]
    if (left != right) // если границы не сомкнулись
    {
      numbers[left] = numbers[right]; // перемещаем элемент [right] на место разрешающего
      count++;
      left++; // сдвигаем левую границу вправо
    }
    while ((numbers[left] <= pivot) && (left < right))
      left++; // сдвигаем левую границу пока элемент [left] меньше [pivot]
    if (left != right) // если границы не сомкнулись
    {
      numbers[right] = numbers[left]; // перемещаем элемент [left] на место [right]
      count++;
      right--; // сдвигаем правую границу влево
    }
  }
  numbers[left] = pivot; // ставим разрешающий элемент на место
  pivot = left;
  left = l_hold;
  right = r_hold;
  if (left < pivot) // Рекурсивно вызываем сортировку для левой и правой части массива
    count += quickSort(numbers, left, pivot - 1);
  if (right > pivot)
    count += quickSort(numbers, pivot + 1, right);
  
  return count;
}
