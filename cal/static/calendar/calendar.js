var data;
const submitData = async () => {
  const date_f = document.getElementById("date").value;
  document.getElementById("date_name").text = date_f;

  axios.post("/calendar/post/", {
      date: date_f,
    })
    .then(
      (res) => {
        data = res.data;
      },
      (error) => {
        console.log(error);
      }
    );
};