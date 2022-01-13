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
      window.location.reload();
    });
  });

  $.get("/cvsDisplay", {}, function (response) {
    let itemListings = response["cleanListing"];
    console.log(itemListings);

    for (let i = 0; i < itemListings.length; i++) {
      let current = itemListings[i];
      let fileItem = current["cleanItem"];
      $("#itemList").append(`-<b>${fileItem}</b><br />`);
      let fileDate = current["cleanDate"];

      let line = `<tr><td><b>${fileItem}</b></td>`;
      line = line + `<td>${fileDate}</td></tr>`;
      $("#inventory").append(line);
    }
  });
  $("#editBtn").click(function () {
    let oldItem = $("#editInput").val();
    let newItem = $("#updateInput").val();

    $.get(
      "/cvsDisplay",
      { oldItem: "oldItem", newItem: "newItem" },
      function (response) {
        console.log(response["inventoryList"]);
        let listing = response["inventoryList"];
        let listingItem = listing[0];
        let listingDate = listing[1];
        let line = `<tr><td>${listingItem}</td></tr>`;
        line = line + `<td>${listingDate}</td>`;
        $("inventory").append(line);
        window.location.reload();
      }
    );
  });

  $("#deleteBtn").click(function () {
    let deleteItem = $("#delInput").val();

    $.get("/edit", { deleteItem: "deleteitem" }, function (response) {
      let listing = response["inventoryList"];
      let listingItem = listing[0];
      let listingDate = listing[1];
      let line = `<tr><td>${listingItem}</td></tr>`;
      line = line + `<td>${listingDate}</td>`;
      $("inventory").append(line);
      window.location.reload();
    });
  });
});
