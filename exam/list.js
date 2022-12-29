// 더보기 버튼 클릭 시 서버로부터 다음 제품 정보 가져오기
// ajax => 1) fetch api(자바스크립트) 2) query

// 더보기 버튼 클릭 시 서버로부터 다음 제품 정보 가져오기
// 더보기 버튼 앞 쪽에 제품 추가

// 더보기 버튼 2번째 누르면 more2.json 가져와서 제품 정보 보여주기
// 더보기 버튼 2번까지만 허용
let cnt = 0;

document.querySelector("#more").addEventListener("click", (e) => {
  cnt += 1;
  let url = cnt == 1 ? "more1.json" : "more2.json";
  fetch(url)
    .then((reposnse) => reposnse.json())
    .then((result) => {
      let products = "";

      result.forEach((item, idx) => {
        products += `<div class="col-sm-4">
            <img src="https://placehold.co/600" alt="" class="w-100" />
            <h5>${item.title}</h5>
            <p>가격:${item.price}</p>
            </div>
            `;
      });
      document.querySelector(".row").insertAdjacentHTML("beforeend", products);

      if (cnt == 2) {
        e.target.disabled = true;
      }
    });
});
