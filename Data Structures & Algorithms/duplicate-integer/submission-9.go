func hasDuplicate(nums []int) bool {
    h := map[int]int{}
	for _,i := range nums{
		if h[i] == 1{
			return true
		}
		h[i] = 1
	}
	return false
}
