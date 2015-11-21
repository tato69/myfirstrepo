clear
$date = Get-Date -format d/M/yyyy
echo "hello, i'm first exercise, today is $date and i'm your master Yoda"
$people = read-host -prompt "how many people are there?"

$count = 0
$names = @()
$ages = @()

do {
	$name = read-host -prompt "enter your name"
	$names += $name
	$age = read-host -prompt "enter your age"
	$ages += $age 
	$count++
}
while ($people -gt $count)

clear

write-output "#################################################################"
write-output "we are in total $people people"
Write-output `n

$count = 0

do {
	$name = $names[$count]
	$age = $ages[$count]
	write-output "i'm $name and i'm $age years old"
	Write-output `n
	$count++
}

while ($people -gt $count)

$agesum = $ages -join '+'
$agesum = invoke-expression $agesum
write-output "the sum of out ages is $agesum"
Write-output `n

$names = $names -join ', '
write-output "our names are $names"
Write-output `n
write-output "#################################################################"