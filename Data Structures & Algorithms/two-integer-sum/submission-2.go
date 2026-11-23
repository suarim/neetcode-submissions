func twoSum(nums []int, target int) []int {
    h := map[int]int{}
	for i,s := range nums{
		print(target-s)
		if _,ok:=h[target - s];ok{
			return []int{h[target-s],i}
		}
		h[s] = i
		
	}
	return []int{1,1}
}
