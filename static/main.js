$(document).ready(function () {
  $("#addItemBtn").click(function () {
    let item = $("#itemInput").val();
    if (item.length == 0) {
      alert("Error: Type in an item");
      return;
    } else {
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
    }
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
    console.log(oldItem.length);
    if (oldItem.length == 0) {
      alert("Error: Type in an item");
      return;
    } else if (newItem.length == 0) {
      alert("Error: type in a new item");
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
    let delItem = $("#delInput").val();
    if (delItem.length == 0) {
      alert("Error: Enter an item to delete");
      return;
    } else {
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
    }
  });
  //From https://codepen.io/brian-guerrero/pen/LZGrJe
  function createCSV(array) {
    var keys = Object.keys(array[0]);
    var result = "";
    result += keys.join(",");
    result += "\n";

    array.forEach(function (item) {
      keys.forEach(function (key) {
        result += item[key] + ",";
      });
      result += "\n";
    });

    return result;
  }
  $("#downloadBtn").click(function () {
    // function downloadCSV(array) {
    $.get("/inventoryFile", {}, function (response) {
      let itemListings = response["cleanListing"];

      //From https://codepen.io/brian-guerrero/pen/LZGrJe
      csv = "data:text/csv;charset=utf-8," + createCSV(itemListings);
      excel = encodeURI(csv);
      link = document.createElement("a");
      link.setAttribute("href", excel);
      link.setAttribute("download", "inventory.csv");
      link.click();
    });
  });
});
