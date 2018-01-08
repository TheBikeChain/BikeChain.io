contract('MyTest', function(accounts) {
  it("should assert true", function(done) {
    var my_test = MyTest.deployed();
    assert.isTrue(true);
    done();
  });
});
