// 14 - bubble, quick, comb, gnome, insert

#include <stdio.h>
#include <stdlib.h>
#define RFACTOR (1.24733)

int bubbleSort(int n, int *a);
int insertionSort(int n, int *mass);
int gnomeSort(int n, int *a);
int quickSort(int *numbers, int left, int right);
int comb_sort(int *array, int n);

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
  FILE* input = fopen("l6v14.txt", "r");
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
  int *comb = numbers;
  int combCount = comb_sort(size, comb);
  print_array(insert, size);
  printf("-------------------------------------------------------\n");
  print_array(bubble, size);
  printf("-------------------------------------------------------\n");
  print_array(gnome, size);
  printf("-------------------------------------------------------\n");
  print_array(comb, size);
  printf("-------------------------------------------------------\n");
  print_array(quick, size);
  printf("-------------------------------------------------------\n");
  printf("bubbleCount : %d", bubbleCount);
  printf("insertCount : %d", insertCount);
  printf("gnomeCount : %d", gnomeCount);
  printf("quickCount : %d", quickCount);
  printf("combCount : %d", combCount);
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

void print_array(int *numbers, int size) {
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
