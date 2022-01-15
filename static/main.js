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
  // function csvDisplay() {
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
  // }
  // csvDisplay();
  // function isEmpty(inputtx) {
  //   if (inputtx.value.length == 0) {
  //     alert("Error: Enter an Item");
  //     return true;
  //   }
  //   return false;
  // }
  $("#editBtn").click(function () {
    let oldItem = $("#editInput").val();
    let newItem = $("#updateInput").val();
    console.log(oldItem.length);
    if (oldItem.length == 0) {
      alert("Error");
      return;
    } else if (newItem.length == 0) {
      alert("Error");
      return;
    } else {
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
    }
  });
  $("#deleteBtn").click(function () {
    if ($("#delInput").length == 0) {
      alert("Error: Enter an item to delete");
    }
    let delItem = $("#delInput").val();
    deleteItem = { delItem: delItem };

    $.get("/delete", deleteItem, function (response) {
      let listing = response["cleanListing"];
      let listingItem = listing[0];
      let listingDate = listing[1];
      let line = `<tr><td>${listingItem}</td></tr>`;
      line = line + `<td>${listingDate}</td>`;
      $("inventory").append(line);
      window.location.reload();
    });
  });
});
