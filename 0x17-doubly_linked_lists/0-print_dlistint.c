#include "lists.h"

/**
 * print_dlistint - all elements of dlistint_t are printed
 *
 * @h: list head
 * return: number of nodes
 */
size_t print_dlistint(const dlistint_t *h)
{
	size_t count = 0;

	while (h != NULL)
	{
		printf("%d\n", h->n);
		h = h->next;
		count++;
	}

	return (count);
}
