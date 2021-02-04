def find_itinerary(flights, current_path):
    if not flights: # We have used up all the flights to construct current path
        return current_path
    last = current_path[-1]
    # Now we look at flights which start at last

    for i, (start,end) in enumerate(flights):
        flights_ex = flights[:i] + flights[i+1:]
        current_path.append(end)
        if start == last:
            return find_itinerary(flights_ex, current_path)
        current_path.pop()
    return None

print(find_itinerary([('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')],['A']))

print(find_itinerary([('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')],['YUL']))






