#include "lists.h"

/**
 * check_cycle - checks if there exists a cycle
 * @lists: pointer to lists first node
 * Return: 1 (SUCESS), 0 (FAIL)
 */

int check_cycle(listint_t *list)
{
	listint_t *slower = list;
	listint_t *faster = list;

	if (!list)
		return (0);

	while (slower && faster && faster->next)
	{
		slower = slower->next;
		faster = faster->next->next;
		if (slower == faster)
			return (1);
	}
	return (0);
}
