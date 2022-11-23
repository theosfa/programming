// 11 - insert, gnome, merge, selection, comb

#include <stdio.h>
#include <stdlib.h>
#define RFACTOR (1.24733)

int insertionSort(int n, int *mass);
int mergeSort(int *a, int l, int r);
int gnomeSort(int n, int *a);
int comb_sort(int *array, int n);
int selectionSort(int *mass, int n);

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
  FILE* input = fopen("l6v11.txt", "r");
  if (input == 0) {
    printf("cant open file\n");
    return 1;
  }
  int size = numberCount(input);
  int numbers[size];
  read_numbers(input, size, numbers);
  int *insert = numbers;
  int insertCount = insertionSort(size, insert);
  int *gnome = numbers;
  int gnomeCount =   gnomeSort(size, gnome);
  int *merge = numbers;
  int mergeCount = mergeSort(merge, 0, size);
  int *comb = numbers;
  int combCount = comb_sort(size, comb);
  int *selection = numbers;
  int selectionCount = selectionSort(merge, size);
  print_array(insert, size);
  printf("-------------------------------------------------------\n");
  print_array(selection, size);
  printf("-------------------------------------------------------\n");
  print_array(gnome, size);
  printf("-------------------------------------------------------\n");
  print_array(merge, size);
  printf("-------------------------------------------------------\n");
  print_array(comb, size);
  printf("-------------------------------------------------------\n");
  printf("selectionCount : %d,\n", selectionCount);
  printf("insertCount : %d,\n", insertCount);
  printf("gnomeCount : %d,\n", gnomeCount);
  printf("combCount : %d,\n", combCount);
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

int comb_sort(int *array, int n){
    int gap = n;
    int count = 0;
    int swaps = 1;
    int i, j;

    while ( gap > 1 || swaps ) {
        gap = (int)(gap / RFACTOR);
        if ( gap < 1 )
            gap = 1;
        swaps = 0;
        for ( i = 0; i < n - gap; ++i ) {
            j = i + gap;
            if ( array[i] > array[j] ) {
                int tmp = array[i];
                array[i] = array[j];
                array[j] = tmp;
                count++;
                swaps = 1;
            }
        }
    }
    return count;
}

int selectionSort(int *mass, int n){
    int minPosition, i, j, tmp;
    int count = 0;
    for (int i = 0; i < n; i++)
    {
        minPosition = i;
        for (int j = i + 1; j < n; j++)
            if (mass[minPosition] > mass[j])
                minPosition = j;
        tmp = mass[minPosition];
        mass[minPosition] = mass[i];
        mass[i] = tmp;
        count++;
    }
    return count;
}
