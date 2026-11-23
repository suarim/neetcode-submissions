import (
	"reflect"
)

func isAnagram(s string, t string) bool {
	x1 := gethaslen(s)
	x2 := gethaslen(t)
	return reflect.DeepEqual(x1,x2)
}

func gethaslen(s string) map[rune]int {
	h := map[rune]int{}
	for _,i := range s{
		if h[i] == 0{
			h[i]=1
		}else{
			h[i]+=1
		}
	}
	return h
}