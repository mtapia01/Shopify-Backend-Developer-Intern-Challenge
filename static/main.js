let itemID = -1;
$(document).ready(function () {
  $("#addItemBtn").click(function () {
    let item = $("#itemInput").val();
    listing = { item: item };

    $.get("/newitem", listing, function (response) {
      console.log(response["inventoryList"]);
      let listing = response["inventoryList"];
      let listingItem = listing[0];
      let listingDate = listing[1];
      let line = `<tr><td>${listingItem}</td></tr>`;
      line = line + `<td>${listingDate}</td>`;
      $("inventory").append(line);
    });
  });

  $.get("/cvsDisplay", {}, function (response) {
    let itemListings = response["cleanListing"];
    console.log(itemListings);

    for (let i = 0; i < itemListings.length; i++) {
      let current = itemListings[i];
      let fileItem = current["cleanItem"];
      let fileDate = current["cleanDate"];

      let line = `<tr><td>${fileItem}</td>`;
      line = line + `<td>${fileDate}</td></tr>`;
      $("#inventory").append(line);
    }
  });

  function getItemList() {
    $.get("/getItemList", {}, function (response) {
      let items = response["items"];

      for (let i = itemID + 1; i < items; i++) {
        let item = items[i]["items"];

        $("#itemList").append(`${item}<br></br>`);
      }
    });
  }
  getItemList();
  setInterval(getItemList, 5000);
  $("#addItemBtn").click(function () {
    let item = $("#itemInput").val();

    $.get("/listOfItems", item, function (response) {
      getItemList();
    });
  });
});
