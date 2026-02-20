# [Silver III] 암호 해독 - 2149 

[문제 링크](https://www.acmicpc.net/problem/2149) 

### 성능 요약

메모리: 32412 KB, 시간: 36 ms

### 분류

구현, 문자열, 정렬

### 제출 일자

2026년 2월 20일 16:49:10

### 문제 설명

<p style="user-select: auto;">어떤 문장을 키를 이용하여 다음과 같이 암호화하려 한다. 암호화하기 전의 문장을 평문이라 하며, 암호화 된 문장은 암호문이라고 한다. 키, 평문, 암호문은 모두 영어 대문자로 된 공백 없는 문장이다.</p>

<p style="user-select: auto;">키의 길이를 N이라고 했을 때, 우선 평문을 N 글자씩 잘라서 다음과 같이 나열한다. 예를 들어 평문이 MEETMEBYTHEOLDOAKTREENTH 이고, 키가 BATBOY라고 해 보자.</p>

<table class="table table-bordered table-center-30 th-center td-center" style="user-select: auto;">
	<tbody style="user-select: auto;">
		<tr style="user-select: auto;">
			<th style="user-select: auto;">B</th>
			<th style="user-select: auto;">A</th>
			<th style="user-select: auto;">T</th>
			<th style="user-select: auto;">B</th>
			<th style="user-select: auto;">O</th>
			<th style="user-select: auto;">Y</th>
		</tr>
		<tr style="user-select: auto;">
			<td style="user-select: auto;">M</td>
			<td style="user-select: auto;">E</td>
			<td style="user-select: auto;">E</td>
			<td style="user-select: auto;">T</td>
			<td style="user-select: auto;">M</td>
			<td style="user-select: auto;">E</td>
		</tr>
		<tr style="user-select: auto;">
			<td style="user-select: auto;">B</td>
			<td style="user-select: auto;">Y</td>
			<td style="user-select: auto;">T</td>
			<td style="user-select: auto;">H</td>
			<td style="user-select: auto;">E</td>
			<td style="user-select: auto;">O</td>
		</tr>
		<tr style="user-select: auto;">
			<td style="user-select: auto;">L</td>
			<td style="user-select: auto;">D</td>
			<td style="user-select: auto;">O</td>
			<td style="user-select: auto;">A</td>
			<td style="user-select: auto;">K</td>
			<td style="user-select: auto;">T</td>
		</tr>
		<tr style="user-select: auto;">
			<td style="user-select: auto;">R</td>
			<td style="user-select: auto;">E</td>
			<td style="user-select: auto;">E</td>
			<td style="user-select: auto;">N</td>
			<td style="user-select: auto;">T</td>
			<td style="user-select: auto;">H</td>
		</tr>
	</tbody>
</table>

<p style="user-select: auto;">제일 윗줄은 이해를 돕기 위해 키를 다시 한 번 쓴 것이다. 이제 이 행렬(배열)을 열(Column) 단위로 정렬을 하는데, 정렬을 하는 키준은 키의 문자로 한다. 즉 BATBOY를 정렬하여 ABBOTY와 같이 정렬하는 것이다. B와 같이 여러 번 나타나는 문자의 경우에는 원래의 행렬에서 더 왼쪽에 있었던 것을 먼저 쓴다. 정렬을 한 행렬은 다음과 같다.</p>

<table class="table table-bordered table-center-30 th-center td-center" style="user-select: auto;">
	<tbody style="user-select: auto;">
		<tr style="user-select: auto;">
			<th style="user-select: auto;">A</th>
			<th style="user-select: auto;">B</th>
			<th style="user-select: auto;">B</th>
			<th style="user-select: auto;">O</th>
			<th style="user-select: auto;">T</th>
			<th style="user-select: auto;">Y</th>
		</tr>
		<tr style="user-select: auto;">
			<td style="user-select: auto;">E</td>
			<td style="user-select: auto;">M</td>
			<td style="user-select: auto;">T</td>
			<td style="user-select: auto;">M</td>
			<td style="user-select: auto;">E</td>
			<td style="user-select: auto;">E</td>
		</tr>
		<tr style="user-select: auto;">
			<td style="user-select: auto;">Y</td>
			<td style="user-select: auto;">B</td>
			<td style="user-select: auto;">H</td>
			<td style="user-select: auto;">E</td>
			<td style="user-select: auto;">T</td>
			<td style="user-select: auto;">O</td>
		</tr>
		<tr style="user-select: auto;">
			<td style="user-select: auto;">D</td>
			<td style="user-select: auto;">L</td>
			<td style="user-select: auto;">A</td>
			<td style="user-select: auto;">K</td>
			<td style="user-select: auto;">O</td>
			<td style="user-select: auto;">T</td>
		</tr>
		<tr style="user-select: auto;">
			<td style="user-select: auto;">E</td>
			<td style="user-select: auto;">R</td>
			<td style="user-select: auto;">N</td>
			<td style="user-select: auto;">T</td>
			<td style="user-select: auto;">E</td>
			<td style="user-select: auto;">H</td>
		</tr>
	</tbody>
</table>

<p style="user-select: auto;">B는 두 가지가 있기 때문에 더 왼쪽에 있었던 (B)MBLR이 먼저 나왔다. 이제 이와 같이 정렬한 행렬을 열 번호가 작은 것 먼저, 열 번호가 같다면 행 번호가 작은 것 순으로 나열하면 암호문이 된다. 즉 위와 같은 경우의 암호문은 EYDEMBLRTHANMEKTETOEEOTH 가 된다.</p>

<p style="user-select: auto;">키와 암호문이 주어졌을 때, 이를 이용하여 평문을 구하는 프로그램을 작성하시오.</p>

### 입력 

 <p style="user-select: auto;">첫째 줄에 키가 주어지고, 둘째 줄에 암호문이 주어진다. 키와 암호문은 모두 영어 대문자로만 되어 있으며, 암호문의 길이가 항상 키의 길이의 배수라고 하자. 키의 길이는 10자 이하이며 암호문의 길이는 100자 이하이다.</p>

### 출력 

 <p style="user-select: auto;">첫째 줄에 평문을 출력한다.</p>

