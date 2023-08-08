#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle
 * @list: pointer to the head of the list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 * description: if first and second pointer meets, there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *first = list;
	listint_t *second = list;

	while (first != NULL && second != NULL && second->next != NULL)
	{
		first = first->next;
		second = second->next->next;

	if (first == second)
		return (1);
	}
	return (0);
}
