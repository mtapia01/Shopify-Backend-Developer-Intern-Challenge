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
      let fileID = current["id"];
      $("#itemList").append(`-<b>${fileItem} ID:${fileID}</b><br />`);
      let fileDate = current["cleanDate"];

      let line = `<tr><td><b>${fileItem}</b></td>`;
      line = line + `<td>${fileDate}</td></tr>`;
      $("#inventory").append(line);
    }
  });
  $("#editBtn").click(function () {
    let oldItem = $("#editInput").val();
    let newItem = $("#updateInput").val();
    editpair = { oldItem: oldItem, newItem: newItem };

    $.get("/edit", editpair, function (response) {
      console.log(response["cleanListing"]);
      let listing = response["cleanListing"];
      let listingItem = listing[0];
      let listingDate = listing[1];
      let line = `<tr><td>${listingItem}</td></tr>`;
      line = line + `<td>${listingDate}</td>`;
      $("inventory").append(line);
      window.location.reload();
    });
  });

  $("#deleteBtn").click(function () {
    let deleteItem = $("#delInput").val();
    deleteEle = { deleteItem: deleteItem };

    $.get("/edit", deleteEle, function (response) {
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
});
